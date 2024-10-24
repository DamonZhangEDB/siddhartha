import os

repo_name = os.getenv("REPO_NAME", "").lower()
run_id = os.getenv("RUN_ID", "").lower()
job_id = os.getenv("JOB_ID", "").lower()

print(f"Repo Name: {repo_name}")
print(f"Run ID: {run_id}")
print(f"Job ID: {job_id}")

run_url = f"https://github.com/{repo_name}/actions/runs/{run_id}/job/{job_id}"

print(f"Run URL: {run_url}")
