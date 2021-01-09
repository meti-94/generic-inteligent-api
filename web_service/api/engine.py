from transformers import BertTokenizerFast, BertForSequenceClassification
from transformers import pipeline
from .serializers import InputJsonSerializer
from django.conf import settings
device = settings.DEVICE
if device!=None:
	device==int(device)
else:
	device=-1


class engine:
	def __init__(self):
		self.model = BertForSequenceClassification.from_pretrained('api/files/sentiment_pipeline/')
		self.tokenizer = BertTokenizerFast.from_pretrained('api/files/sentiment_pipeline/')
		self.pipeline = pipeline("sentiment-analysis",return_all_scores=True,  
								 model=self.model, tokenizer=self.tokenizer,
								 device=device)


	def predict(self, _input):
		text = _input['docBody']
		return [item['score'] for item in self.pipeline(text)[0]]

	def predict_batch(self, _input_list):
		texts_list = [item['docBody'] for item in _input_list]
		probs = [[item[0]['score'], item[1]['score']] for item in self.pipeline(texts_list)]
		return probs


if __name__=='__main__':
	eng = engine()
	