# A wrapper around pip package to pull in undeclared dependencies.

load("@programl_requirements//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

licenses(["notice"])  # BSD

py_library(
    name = "scikit_learn",
    srcs = ["//third_party/py:empty.py"],
    deps = [
        requirement("scikit-learn"),
        requirement("joblib"),
        "//third_party/py/scipy",
    ],
)
