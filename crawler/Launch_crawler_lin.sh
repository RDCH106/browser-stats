#!/bin/bash

scrapy crawl browser-stats -t json -o - > browser-stats.json
read -p "Press [Enter] key to continue..."