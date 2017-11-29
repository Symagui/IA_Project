# coding: utf8

from sklearn.feature_extraction import DictVectorizer

def computeDico(values, names) :
	return [dict(zip(names, value)) for value in values]

def computeInputTreeArray(dicoList) :
	vec = DictVectorizer()
	array =  vec.fit_transform(dicoList).toarray()
	return vec, array

def transform(values, names) :
	return computeInputTreeArray(computeDico(values, names))

def transform_test(values, names, tranformer) :
	return tranformer.transform(computeDico(values, names)).toarray()