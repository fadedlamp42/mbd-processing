all: download process graph

download:
	clear
	@sh ./scripts/download.sh

process:
	clear
	@sh ./scripts/process.sh

graph: 
	clear
	@sh ./scripts/graph.sh

clean:
	clear
	@sh ./scripts/clean.sh
