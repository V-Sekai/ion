#
# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# This file gets included only for Linux targets.

{
  'variables': {
    'compiler_dir': '/usr',
  },
  'make_global_settings' : [
    #['CC', '<(compiler_dir)/bin/clang'],
    #['CXX', '<(compiler_dir)/bin/clang++'],
    #['LINK', '<(compiler_dir)/bin/clang++'],
    ['CC', '<(compiler_dir)/bin/gcc'],
    ['CXX', '<(compiler_dir)/bin/g++'],
    ['LINK', '<(compiler_dir)/bin/g++'],
  ],
  'target_defaults': {
    'library_dirs': [
      '/usr/lib/x86_64-linux-gnu',
    ],
  },
}
