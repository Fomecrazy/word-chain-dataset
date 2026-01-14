import json
from datetime import datetime, timezone
import os

subsetGroups = [
	list(range(0, 18)),
	list(range(18, 25)),
	list(range(25, 35)),
	list(range(35, 42)),
	list(range(42, 45)),
]

sha = os.environ.get("AFTER_SHA")

try:
	with open("data/dataset/curated/blacklist.json", "r", encoding="utf-8") as f:
		blacklist = json.load(f)
except:
	blacklist = {}


def isUpdated(path, chains):
	try:
		with open(path, "r", encoding="utf-8") as f:
			data = json.load(f)

			a_normalized = {k: set(v) for k, v in data["data"].items()}
			b_normalized = {k: set(v) for k, v in chains.items()}

			return a_normalized != b_normalized
	except:
		return True
	
	return False

def compileSubsets():
	os.makedirs("data/dataset/generated", exist_ok=True)
	
	changed = []
	for i in range(len(subsetGroups)):
		subsets = subsetGroups[i]
		chains = {}

		for j in range(len(subsets) - 1):
			curr = subsets[j]
			next = subsets[j + 1]

			with open(f"data/subsets/subset{curr}.txt", "r", encoding="utf-8") as f:
				currWords = [line.strip() for line in f if line.strip()]
			with open(f"data/subsets/subset{next}.txt", "r", encoding="utf-8") as f:
				nextWords = [line.strip() for line in f if line.strip()]

			for word in currWords:
				if not word in chains: chains[word] = []
				blacklistDict = blacklist.get(word) or []

				for chained in nextWords:
					if chained in blacklistDict or chained in chains[word]: continue
					chains[word].append(chained)

		path = f"data/dataset/generated/generated{i}.json"
		if not isUpdated(path, chains): continue

		dataset = {
			"version": sha,
			"updated_at": datetime.now(timezone.utc).isoformat(),
			"data": chains,
		}
		changed.append(path)

		with open(path, "w", encoding="utf-8") as f:
			json.dump(dataset, f, indent=2, ensure_ascii=False)

compileSubsets()