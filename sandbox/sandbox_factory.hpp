#pragma once

#include <sandbox/sandbox.hpp>

namespace sandbox {

class SandboxFactory {

public:
    static std::unique_ptr<Sandbox> create();

};

}
