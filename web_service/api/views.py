from django.conf import settings
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import InputJsonSerializer, OutputJsonSerializer
from .engine import engine


batch_size = settings.BATCH_SIZE
lang = settings.LANG
eng = engine()



def batchify(l, n): 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 


@api_view(['POST'])
def main(request):
	serialized_request = InputJsonSerializer(data=request.data)
	if serialized_request.is_valid():
		request_data = serialized_request.validated_data
		if request_data['lang']!= lang:
			return Response({'Error':'Wrong language!'})
		probs = eng.predict(request_data)
		if max(probs)-min(probs)>0.33:
			conf = round(max(probs)*100)
			label = probs.index(max(probs))
			if label==1:
				_response = {'confidence':conf, 'label':'positive'}
				output_serializer = OutputJsonSerializer(_response)
				return Response(output_serializer.data)
			else:
				_response = {'confidence':conf, 'label':'negative'}
				output_serializer = OutputJsonSerializer(_response)
				return Response(output_serializer.data)
		else:
			conf = round(max(probs)*100)
			_response = {'confidence':conf+32, 'label':'neutral'}
			output_serializer = OutputJsonSerializer(_response)
			return Response(output_serializer.data)
	else:
		return Response(serialized_request.errors())


@api_view(['POST'])
def main_batch(request):
	serialized_request = InputJsonSerializer(data=request.data, many=True)
	if serialized_request.is_valid():
		request_data = serialized_request.validated_data
		length = len(request_data)
		if length==0:
			return Response({'Error':'Batch Is Empty!'})
		for item in request_data:
			if item['lang']!= lang:
				return Response({'Error':'Wrong language!'})
		_response = []
		batches = list(batchify(request_data, batch_size))
		for batch in batches:
			# batch = request_data[index*batch_size:min((index+1)*batch_size, length)]
			probs_list = eng.predict_batch(batch)
			for probs in probs_list:
				if max(probs)-min(probs)>0.33:
					conf = round(max(probs)*100)
					label = probs.index(max(probs))
					if label==1:
						temp_response = {'confidence':conf, 'label':'positive'}
						_response.append(temp_response)
					else:
						temp_response = {'confidence':conf, 'label':'negative'}
						_response.append(temp_response)
				else:
					conf = round(max(probs)*100)
					temp_response = {'confidence':conf+32, 'label':'neutral'}
					_response.append(temp_response)
		output_serializer = OutputJsonSerializer(_response, many=True)
		return Response(output_serializer.data)
	else:
		return Response(serialized_request.errors())
