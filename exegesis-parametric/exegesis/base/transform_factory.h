// Copyright 2016 Google Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// This file contains utilities to create transforms from flags.

#ifndef EXEGESIS_BASE_TRANSFORM_FACTORY_H_
#define EXEGESIS_BASE_TRANSFORM_FACTORY_H_

#include <string>
#include <vector>

#include "absl/flags/declare.h"
#include "exegesis/base/cleanup_instruction_set.h"

ABSL_DECLARE_FLAG(std::string, exegesis_transforms);

namespace exegesis {

// Returns a vector of transforms corresponding to transformations given in
// --exegesis_transforms.
std::vector<InstructionSetTransform> GetTransformsFromCommandLineFlags();

}  // namespace exegesis

#endif  // EXEGESIS_BASE_TRANSFORM_FACTORY_H_
