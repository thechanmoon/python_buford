from extractors.wwr import extract_jobs

# pkgs.chromium
# pkgs.chromedriver

jobs = extract_jobs("python")

print(jobs)

# for num in range(9):
#     print(f"2 x {num+1} = {2*(num+1)}")
