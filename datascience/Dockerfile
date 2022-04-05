FROM jupyter/base-notebook:python-3.9.10 as train

COPY --chown=jovyan:users setup.py .
COPY --chown=jovyan:users scripts/ scripts/

RUN pip install '.[train]' && python scripts/download_nltk.py
RUN wget -O pizza_data.json "https://drive.google.com/uc?export=download&id=13wX6U3-PCv5QE_1E2sFSgQY9FmdGdr6z"
COPY --chown=jovyan:users raopred/ raopred/
COPY --chown=jovyan:users research/ research/
RUN mv pizza_data.json research/
RUN echo $USER

FROM train as test
COPY tests/ tests/