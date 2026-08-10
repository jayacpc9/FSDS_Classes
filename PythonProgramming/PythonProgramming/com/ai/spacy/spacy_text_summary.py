import nltk
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
import subprocess

# This runs the command as if you typed it in your terminal
subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])

text = """There are broadly two types of extractive summarization tasks depending on what the summarization program focuses on. The first is generic summarization, which focuses on obtaining a generic summary or abstract of the collection (whether documents, or sets of images, or videos, news stories etc.). The second is query relevant summarization, sometimes called query-based summarization, which summarizes objects specific to a query. Summarization systems are able to create both query relevant text summaries and generic machine-generated summaries depending on what the user needs.
An example of a summarization problem is document summarization, which attempts to automatically produce an abstract from a given document. Sometimes one might be interested in generating a summary from a single source document, while others can use multiple source documents (for example, a cluster of articles on the same topic). This problem is called multi-document summarization. A related application is summarizing news articles. Imagine a system, which automatically pulls together news articles on a given topic (from the web), and concisely represents the latest news as a summary.
Image collection summarization is another application example of automatic summarization. It consists in selecting a representative set of images from a larger set of images.[4] A summary in this context is useful to show the most representative images of results in an image collection exploration system. Video summarization is a related domain, where the system automatically creates a trailer of a long video. This also has applications in consumer or personal videos, where one might want to skip the boring or repetitive actions. Similarly, in surveillance videos, one would want to extract important and suspicious activity, while ignoring all the boring and redundant frames captured """

print("Character langth = ", len(text))
print("Word length = ", len(text.split(' ')))
print("Full text = ", text)

stopwords = list(STOP_WORDS)
print("Stop words length = ", len(stopwords))
print(stopwords)


def load_user_text(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    print(type(doc))
    tokens = [tokens.text for tokens in doc]
    print(tokens)
    return doc


def get_word_frequency(doc):
    word_frequencies = {}

    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1

    print('Length of word frequencies = ', len(word_frequencies))
    print(word_frequencies)

    max_frequency = max(word_frequencies.values())
    print(max_frequency)

    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / max_frequency
    print(word_frequencies)
    return word_frequencies


def calculate_sentence_score(doc, word_frequencies):
    sentences_tokens = [sentence for sentence in doc.sents]
    print("Total no of Senctences = ", len(sentences_tokens))
    print(sentences_tokens)
    sentence_scores = {}
    for sent in sentences_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]
    print("len(sentence_scores) = ", len(sentence_scores))
    print(sentence_scores)
    return sentence_scores, sentences_tokens


def generate_final_summary(sentences_tokens, sentence_scores, summary_percentage):
    from heapq import nlargest
    print("Generating final summary ...")
    print("len(sentences_tokens) = ", len(sentences_tokens))
    select_length = int(len(sentences_tokens) * summary_percentage)
    print(select_length)

    summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
    print("len(summary) = ", len(summary))
    print(summary)

    final_summary = [sent.text for sent in summary]
    print(type(final_summary)," : ",len(final_summary))
    return " ".join(final_summary)


def generate_user_text_summary(text, summary_percentage):
    doc = load_user_text(text)
    word_frequencies = get_word_frequency(doc)
    sentence_scores, sentences_tokens = calculate_sentence_score(doc, word_frequencies)
    summary = generate_final_summary(sentences_tokens, sentence_scores, (summary_percentage / 10))
    return summary


print("Final Summary = ",generate_user_text_summary(text,3))
