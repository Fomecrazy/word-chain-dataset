import json
import subprocess
import os
from datetime import datetime, timezone

try:
	with open("data/dataset/curated/blacklist.json", "r", encoding="utf-8") as f:
		blacklist = json.load(f)
except:
	blacklist = {}
try:
	with open("manifest.json", "r", encoding="utf-8") as f:
		manifestData = json.load(f)["dataset"]
except:
	manifestData = {}

try:
	prevSHA = subprocess.check_output(
    	["git", "log", "-n", "1", "--pretty=format:%H", "manifest.json"]
			).decode().strip()
	if prevSHA == "0": prevSHA = "4b825dc642cb6eb9a060e54bf8d69288fbee4904"

	currentSHA = subprocess.check_output(
	["git", "rev-parse", "HEAD"]
		).decode().strip()
	
except:
	raise Exception("Failed to get previous or current commit SHA")

def getRawUrl(path):
	return f"https://raw.githubusercontent.com/Fomecrazy/word-chain-dataset/{currentSHA}/{path}"

def updateManifest():
	datasetData = manifestData
	changed_files = []
	try:
		diff = subprocess.check_output(
		["git", "diff", "--name-only", prevSHA, currentSHA, "--", "data/dataset"]
			).decode().splitlines()
		
		print(diff)

		exclude = set(["data/dataset/curated/blacklist.json", "data/dataset/generated/deadEnds.json"])

		changed_files = [f for f in diff if not f in exclude]
	except subprocess.CalledProcessError as e:
		print(e.output.decode())

	for root, _, datasets in os.walk("data/dataset"):
		for d in datasets:
			path = os.path.join(root, d).replace("\\", "/")
			if not os.path.isfile(path) or not path in changed_files: continue

			datasetData[os.path.splitext(d)[0]] = {
				"version": currentSHA,
				"updated_at": datetime.now(timezone.utc).isoformat(),
				"url": getRawUrl(path),
			}

			try:
				# if root == "data/dataset/generated": continue

				with open(path, "r", encoding="utf-8") as f:
					data = json.load(f)
					data["version"] = currentSHA
					data["updated_at"] = datetime.now(timezone.utc).isoformat()

				with open(path, "w", encoding="utf-8") as f:
					json.dump(data, f, indent=2, ensure_ascii=False)
			except: continue

	manifest = {
		"version": currentSHA,
		"updated_at": datetime.now(timezone.utc).isoformat(),
		"dataset": datasetData,
	}

	with open("manifest.json", "w", encoding="utf-8") as f:
		json.dump(manifest, f, indent=2, ensure_ascii=False)

updateManifest()