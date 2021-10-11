#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
from openqa_client.client import OpenQA_Client

if __name__ == "__main__":
    distri = "opensuse"
    version = "Tumbleweed"
    build = "20210921"
    job_group = 1

    ooo = OpenQA_Client(server="openqa.opensuse.org", scheme="https")

    # Note: '/api/v1' is added automatically, if the path does not start with /
    path = "jobs/overview"
    params = {}
    params['distri'] = distri
    params['version'] = version
    params['build'] = build
    params['job_group'] = job_group

    c_group = ooo.openqa_request(method="GET", path=path, params=params)
    # print(json.dumps(c_group))

    job_ids = [job["id"] for job in c_group]
    jobs = ooo.get_jobs(jobs=job_ids)
    for job in jobs:
        name = job["name"]
        state = job["state"]
        print("%-100s\t%-20s" % (name, state))
