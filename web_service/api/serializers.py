from rest_framework import serializers



class InputJsonSerializer(serializers.Serializer):
    lang = serializers.ChoiceField(['fa', 'en'])
    docType = serializers.IntegerField(max_value=None, min_value=0, required=False)
    docTitle = serializers.CharField(trim_whitespace=True, allow_blank=True, allow_null=True, required=False)
    docBody = serializers.CharField(allow_blank=False, trim_whitespace=True)
    docSummary = serializers.CharField(trim_whitespace=True, allow_blank=True, allow_null=True, required=False)
    docTags = serializers.ListField(child=serializers.CharField(), allow_empty=True, allow_null=True)




class OutputJsonSerializer(serializers.Serializer):
    confidence = serializers.IntegerField(min_value=0, max_value=100)
    label = serializers.ChoiceField(['positive', 'negative', 'neutral'])

