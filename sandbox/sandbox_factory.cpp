#include <sandbox/sandbox_factory.hpp>

#include <sandbox/podman/podman_sandbox.hpp>

namespace sandbox {

std::unique_ptr<Sandbox> SandboxFactory::create() {

    return std::make_unique<PodmanSandbox>();

}

}
