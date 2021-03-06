# Graph-based Machine Learning for Programming Languages.
# https://chriscummins.cc/ProGraML/
#
# Copyright 2019-2020 the ProGraML authors.
#
# Contact Chris Cummins <chrisc.101@gmail.com>.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

exports_files([
    ".bettercodehub.yml",
    "CONTRIBUTING.md",
    "LICENSE",
    "README.md",
    "version.txt",
    "WORKSPACE",
])

config_setting(
    name = "darwin",
    values = {"cpu": "darwin"},
    visibility = ["//visibility:public"],
)

sh_binary(
    name = "install",
    srcs = ["install.sh"],
    data = [
        ":package",
        "@bazel_tools//tools/bash/runfiles",
    ],
)

genrule(
    name = "package",
    srcs = [
        "//bin:analyze",
        "//bin:graph2cdfg",
        "//bin:clang2graph-10",
        "//bin:graph2dot",
        "//bin:graph2json",
        "//bin:llvm2graph-10",
        "//bin:pbq",
        "//bin:xla2graph",
        ":LICENSE",
        ":version.txt",
    ] + select({
        "//:darwin": [
            "@clang-llvm-10.0.0-x86_64-apple-darwin//:libs",
            "@clang-llvm-10.0.0-x86_64-apple-darwin//:libdir",
        ],
        "//conditions:default": [
            "@clang-llvm-10.0.0-x86_64-linux-gnu-ubuntu-18.04//:lib",
            "@clang-llvm-10.0.0-x86_64-linux-gnu-ubuntu-18.04//:libdir",
        ],
    }),
    outs = ["package.tar.bz2"],
    cmd = (
              # Create the LICENSE and README files.
              "mkdir package && " +
              "cp $(location :LICENSE) package && " +
              "echo \"ProGraML version $$(tr -d '\n' < $(location :version.txt)) <http://github.com/ChrisCummins/ProGraML>\" > package/README &&"
          ) + (
              # Copy the binaries to package/bin.
              "rsync -ah --copy-links $$(dirname $(location //bin:graph2dot)) package &&"
          ) + (
              # Create the clang2graph and llvm2graph symlinks in package/bin.
              "ln -s clang2graph-10 package/bin/clang2graph &&" +
              "ln -s llvm2graph-10 package/bin/llvm2graph &&"
          ) +
          select({
              # Copy the LLVM libraries to package/llvm.
              "//:darwin": "rsync -ah --copy-links --exclude '*.a' --exclude '*.cmake' --exclude '*.h' $(location @clang-llvm-10.0.0-x86_64-apple-darwin//:libdir) package &&",
              "//conditions:default": "rsync -ah --copy-links --exclude '*.a' --exclude '*.cmake' --exclude '*.h' $(location @clang-llvm-10.0.0-x86_64-linux-gnu-ubuntu-18.04//:libdir) package &&",
          }) + (
              # NOTE(github.com/ChrisCummins/ProGraML/issues/134): Workaround for load-time errors
              # when systems expect LLVMPolly.so to have the "lib" name prefix.
              "ln -s LLVMPolly.so package/lib/libLLVMPolly.so &&"
          ) +
          (
              # Create the package archive.
              "tar cjf $@ -C package ."
          ),
)
