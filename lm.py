import string
import random
import math
import messageParser
import config


def tokenize(text):
    text = text.strip()
    tokens = []
    punctuation = set(string.punctuation)
    split_chars = punctuation.union(set(string.whitespace))
    temp_token_chars = []

    for c in text:

        if c in split_chars:
            if temp_token_chars:
                temp_token = "".join(temp_token_chars)
                tokens.append(temp_token)

            if c in punctuation:
                tokens.append(c)

            temp_token_chars = []
        else:
            temp_token_chars.append(c)


    if temp_token_chars:
        temp_token = "".join(temp_token_chars)
        tokens.append(temp_token)

    return tokens
        

def ngrams(n, tokens):
    start = ["<START>" for i in range(n-1)]

    ngrams_list = []

    for token in tokens + ["<END>"]:
        ngram = (tuple(start), token)
        ngrams_list.append(ngram)

        if n > 1:
            start = start[1:]
            start.append(token)

    return ngrams_list
        

class NgramModel(object):

    def __init__(self, n):
        self.n = n
        self.ngrams_tracker = dict()

    def update(self, sentence):
        tokens = tokenize(sentence)
        ngrams_list = ngrams(self.n, tokens)

        for ngram in ngrams_list:
            context = ngram[0]
            token = ngram[1]

            if context not in self.ngrams_tracker:
                self.ngrams_tracker[context] = [token]
            else:
                self.ngrams_tracker[context].append(token)

    def prob(self, context, token):
        tokens_for_context = self.ngrams_tracker[context]
        total = len(tokens_for_context)

        count = 0

        for item in tokens_for_context:
            if token == item:
                count += 1

        return count/total

    def random_token(self, context):

        r = random.random()

        tokens_for_context = set(self.ngrams_tracker[context])

        tokens_for_context = sorted(list(tokens_for_context))

        total_prob = 0

        for token in tokens_for_context:
            token_prob = self.prob(context, token)
            total_prob += token_prob
            if total_prob > r:
                return token

    def reset_context(self):
        return ["<START>" for i in range(self.n-1)]

    def random_text(self, token_count):
        context = self.reset_context()

        tokens = []

        for i in range(token_count):
            new_token = self.random_token(tuple(context))

            if new_token == "<END>":
                if len(tokens) > 0:
                    break
                else:
                    context = self.reset_context()
            else:
                tokens.append(new_token)
                if self.n > 1:
                    context = context[1:]
                    context.append(new_token)

        return " ".join(tokens)

def create_ngram_model(n, path):

    m = NgramModel(n)

    my_name = config.my_name
    buddy_name = config.buddy_name
    buddy_number = config.buddy_number

    for message in messageParser.parse_all_html_files(path):
        m.update(message.get_msg_text())

    for message in messageParser.parse_all_xml_files(path, my_name, buddy_name, buddy_number):
        m.update(message.get_msg_text())

    return m
