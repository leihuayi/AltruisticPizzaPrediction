FROM jupyter/base-notebook:python-3.9.10 as train

COPY --chown=jovyan:users setup.py .
COPY --chown=jovyan:users scripts/ scripts/

# install python dependancies
RUN pip install '.[train]' && python scripts/download_nltk.py

# install files
RUN wget -O pizza_data.json "https://drive.google.com/uc?export=download&id=13wX6U3-PCv5QE_1E2sFSgQY9FmdGdr6z" \
    && wget -O model.pickle "https://drive.google.com/uc?export=download&id=1DbfCvaUMfJcBclHUq1E75HRF6M7Yo5tv" \
    && wget -O vectorizer.pickle "https://drive.google.com/uc?export=download&id=1dSGcBNPCDtLZwUc9yYtaev3xzYzGpaqS" \
COPY --chown=jovyan:users raopred/ raopred/
COPY --chown=jovyan:users research/ research/
RUN mv pizza_data.json research/ \
    && mkdir raopred/pickles/ \
    && mv *.pickle raopred/pickles/

FROM train as test
COPY tests/ tests/