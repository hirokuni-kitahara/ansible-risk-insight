# -*- mode:python; coding:utf-8 -*-

# Copyright (c) 2022 IBM Corp. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dataclasses import dataclass, field
import jsonpickle


@dataclass
class Findings:
    metadata: dict = field(default_factory=dict)
    dependencies: list = field(default_factory=list)

    root_definitions: dict = field(default_factory=dict)
    ext_definitions: dict = field(default_factory=dict)
    extra_requirements: list = field(default_factory=list)
    resolve_failures: dict = field(default_factory=dict)

    prm: dict = field(default_factory=dict)
    report: dict = field(default_factory=dict)

    summary_txt: str = ""

    def simple(self):
        d = self.report.copy()
        d["metadata"] = self.metadata
        d["dependencies"] = self.dependencies
        return d

    def dump(self, fpath=""):
        json_str = jsonpickle.encode(self, make_refs=False)
        if fpath:
            with open(fpath, "w") as file:
                file.write(json_str)
        return json_str

    @staticmethod
    def load(fpath="", json_str=""):
        if fpath:
            with open(fpath, "r") as file:
                json_str = file.read()
        findings = jsonpickle.decode(json_str)
        return findings
