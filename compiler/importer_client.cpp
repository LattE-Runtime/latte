#include <spdlog/spdlog.h>
#include <spdlog/sinks/stdout_color_sinks.h>
#include <sandbox/sandbox.hpp>
#include <cstdlib>

#include <compiler/importer_client.hpp>

namespace compiler {

void ImporterClient::fetch(const std::string& model_id)
{
    spdlog::info("[ImporterClient::fetch] Fetching model_id = {}", model_id);
    
    std::filesystem::path home = std::getenv("HOME");

    sandbox::SandboxConfig config {
        .image = "latte-roaster",
        .env = std::map<std::string, std::string>{
            {"MODEL_ID", model_id}
        },
        .network_enabled = true,
        .mounts = {
            sandbox::Mount {
                .host_path = home / ".latte/models/hf" / model_id,
                .sandbox_path = "/app/model",
                .mode = sandbox::MountMode::ReadWrite
            }
        }
    };

    int exit_code = m_sandbox->run(config)->wait();

    spdlog::info("[ImporterClient::fetch] Model grind process exited with status code {}", exit_code);
}

}
