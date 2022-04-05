# Data science projet for predicting Random Acts of Pizza (RAOPred)

## Usage for development

**Develop with jupyter notebook**
```bash
docker-compose build notebook
docker-compose up notebook
```

**Run tests**
```bash
docker-compose build tests
docker-compose up tests
```

> If you have an error "Download models", run `./download_models.sh` .

## Package usage
**Install**
```bash
pip install --index-url https://test.pypi.org/simple/ raopred==0.0.4
```

**Import in Python**
```python
from raopred import predict

text = "I would like a pizza so much please. I would not know how to thank you if you can forward me a pizza. \
            I'll definitely pay you back my friend. Thanks !! https://myphoto.com"
title = "[Request] I really want some food please"
len_text = len(text)
number_of_downvotes = 2
number_of_upvotes = 8
request_number_of_comments = 4
inp = [title+' '+text, len_text, number_of_downvotes, number_of_upvotes, request_number_of_comments]

label = predict(inp)
print(label)
```
```bash
>>> True
```