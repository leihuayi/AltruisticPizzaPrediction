#!/bin/bash
mkdir raopred/pickles
apt-get update && apt-get install wget
wget -O raopred/pickles/model.pickle "https://drive.google.com/uc?export=download&id=1DbfCvaUMfJcBclHUq1E75HRF6M7Yo5tv"
wget -O raopred/pickles/vectorizer.pickle "https://drive.google.com/uc?export=download&id=1dSGcBNPCDtLZwUc9yYtaev3xzYzGpaqS"
