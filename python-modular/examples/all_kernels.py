#!/usr/bin/env python
"""
Explicit examples on how to use the different kernels
"""

from sys import maxint
from numpy import ubyte, ushort, double, int, zeros, sum, floor, array, arange
from numpy.random import randint, rand, seed
from shogun.PreProc import SortWordString, SortUlongString
from shogun.Distance import EuclidianDistance
from shogun.Classifier import PluginEstimate
from shogun.Kernel import *
from shogun.Features import *

def get_dna ():
	acgt=array(['A', 'C', 'G','T'])
	len_acgt=len(acgt)
	rand_train=[]
	rand_test=[]

	for i in xrange(11):
		str1=[]
		str2=[]
		for j in range(60):
			str1.append(acgt[floor(len_acgt*rand())])
			str2.append(acgt[floor(len_acgt*rand())])
		rand_train.append(''.join(str1))
	rand_test.append(''.join(str2))
	
	for i in xrange(6):
		str1=[]
		for j in range(60):
			str1.append(acgt[floor(len_acgt*rand())])
	rand_test.append(''.join(str1))

	return {'train': rand_train, 'test': rand_test}

###########################################################################
# byte features
###########################################################################

def linear_byte ():
	print 'LinearByte'
	
	num_feats=11
	data=randint(0, maxint, (num_feats, 11)).astype(ubyte)
	feats_train=ByteFeatures(data, RAWBYTE)
	data=randint(0, maxint, (num_feats, 17)).astype(ubyte)
	feats_test=ByteFeatures(data, RAWBYTE)
	
	kernel=LinearByteKernel(feats_train, feats_train)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

###########################################################################
# real features
###########################################################################

def chi2 ():
	print 'Chi2'

	num_feats=11
	data=rand(num_feats, 11)
	feats_train=RealFeatures(data)
	data=rand(num_feats, 17)
	feats_test=RealFeatures(data)
	width=1.4
	size_cache=10
	
	kernel=Chi2Kernel(feats_train, feats_train, width, size_cache)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

def const ():
	print 'Const'

	num_feats=11
	data=rand(num_feats, 11)
	feats_train=RealFeatures(data)
	data=rand(num_feats, 17)
	feats_test=RealFeatures(data)
	c=23.

	kernel=ConstKernel(feats_train, feats_train, c)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

def diag ():
	print 'Diag'

	num_feats=11
	data=rand(num_feats, 11)
	feats_train=RealFeatures(data)
	data=rand(num_feats, 17)
	feats_test=RealFeatures(data)
	diag=23.

	kernel=DiagKernel(feats_train, feats_train, diag)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

def gaussian ():
	print 'Gaussian'

	num_feats=11
	data=rand(num_feats, 11)
	feats_train=RealFeatures(data)
	data=rand(num_feats, 17)
	feats_test=RealFeatures(data)
	width=1.9

	kernel=GaussianKernel(feats_train, feats_train, width)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

def gaussian_shift ():
	print 'GaussianShift'

	num_feats=11
	data=rand(num_feats, 11)
	feats_train=RealFeatures(data)
	data=rand(num_feats, 17)
	feats_test=RealFeatures(data)
	width=1.8
	max_shift=2
	shift_step=1

	kernel=GaussianShiftKernel(
		feats_train, feats_train, width, max_shift, shift_step)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

def linear ():
	print 'Linear'

	num_feats=11
	data=rand(num_feats, 11)
	feats_train=RealFeatures(data)
	data=rand(num_feats, 17)
	feats_test=RealFeatures(data)
	scale=1.2

	kernel=LinearKernel(feats_train, feats_train, scale)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

def poly ():
	print 'Poly'

	num_feats=11
	data=rand(num_feats, 11)
	feats_train=RealFeatures(data)
	data=rand(num_feats, 17)
	feats_test=RealFeatures(data)
	degree=4
	inhomogene=False
	use_normalization=True
	
	kernel=PolyKernel(
		feats_train, feats_train, degree, inhomogene, use_normalization)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

def sigmoid ():
	print 'Sigmoid'

	num_feats=11
	data=rand(num_feats, 11)
	feats_train=RealFeatures(data)
	data=rand(num_feats, 17)
	feats_test=RealFeatures(data)
	size_cache=10
	gamma=1.2
	coef0=1.3

	kernel=SigmoidKernel(feats_train, feats_train, size_cache, gamma, coef0)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

###########################################################################
# sparse real features
###########################################################################

def sparse_gaussian ():
	print 'SparseGaussian'

	num_feats=11
	data=rand(num_feats, 11)
	feat=RealFeatures(data)
	feats_train=SparseRealFeatures()
	feats_train.obtain_from_simple(feat)
	data=rand(num_feats, 17)
	feat=RealFeatures(data)
	feats_test=SparseRealFeatures()
	feats_test.obtain_from_simple(feat)
	width=1.1

	kernel=SparseGaussianKernel(feats_train, feats_train, width)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

def sparse_linear ():
	print 'SparseLinear'

	num_feats=11
	data=rand(num_feats, 11)
	feat=RealFeatures(data)
	feats_train=SparseRealFeatures()
	feats_train.obtain_from_simple(feat)
	data=rand(num_feats, 17)
	feat=RealFeatures(data)
	feats_test=SparseRealFeatures()
	feats_test.obtain_from_simple(feat)
	scale=1.1

	kernel=SparseLinearKernel(feats_train, feats_train, scale)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

def sparse_poly ():
	print 'SparsePoly'

	num_feats=11
	data=rand(num_feats, 11)
	feat=RealFeatures(data)
	feats_train=SparseRealFeatures()
	feats_train.obtain_from_simple(feat)
	data=rand(num_feats, 17)
	feat=RealFeatures(data)
	feats_test=SparseRealFeatures()
	feats_test.obtain_from_simple(feat)
	size_cache=10
	degree=3
	inhomogene=True
	use_normalization=False

	kernel=SparsePolyKernel(feats_train, feats_train, size_cache, degree,
		inhomogene, use_normalization)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

###########################################################################
# word features
###########################################################################

def linear_word ():
	print 'LinearWord'

	maxval=2**16-1
	num_feats=11
	data=randint(0, maxval, (num_feats, 11)).astype(ushort)
	feats_train=WordFeatures(data)
	data=randint(0, maxval, (num_feats, 17)).astype(ushort)
	feats_test=WordFeatures(data)
	do_rescale=True
	scale=1.4

	kernel=LinearWordKernel(feats_train, feats_train, do_rescale, scale)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

def poly_match_word ():
	print 'PolyMatchWord'

	maxval=2**16-1
	num_feats=11
	data=randint(0, maxval, (num_feats, 11)).astype(ushort)
	feats_train=WordFeatures(data)
	data=randint(0, maxval, (num_feats, 17)).astype(ushort)
	feats_test=WordFeatures(data)
	degree=2
	inhomogene=True

	kernel=PolyMatchWordKernel(feats_train, feats_train, degree, inhomogene)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

def word_match ():
	print 'WordMatch'

	maxval=2**16-1
	num_feats=11
	data=randint(0, maxval, (num_feats, 11)).astype(ushort)
	feats_train=WordFeatures(data)
	data=randint(0, maxval, (num_feats, 17)).astype(ushort)
	feats_test=WordFeatures(data)
	degree=3
	do_rescale=True
	scale=1.4

	kernel=WordMatchKernel(feats_train, feats_train, degree, do_rescale, scale)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

###########################################################################
# string features
###########################################################################

def fixed_degree_string ():
	print 'FixedDegreeString'

	data=get_dna()
	feats_train=StringCharFeatures(DNA)
	feats_train.set_string_features(data['train'])
	feats_test=StringCharFeatures(DNA)
	feats_test.set_string_features(data['test'])
	degree=3

	kernel=FixedDegreeStringKernel(feats_train, feats_train, degree)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

def linear_string ():
	print 'LinearString'

	data=get_dna()
	feats_train=StringCharFeatures(DNA)
	feats_train.set_string_features(data['train'])
	feats_test=StringCharFeatures(DNA)
	feats_test.set_string_features(data['test'])

	kernel=LinearStringKernel(feats_train, feats_train)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

def local_alignment_string():
	print 'LocalAlignmentString'

	data=get_dna()
	feats_train=StringCharFeatures(DNA)
	feats_train.set_string_features(data['train'])
	feats_test=StringCharFeatures(DNA)
	feats_test.set_string_features(data['test'])

	kernel=LocalAlignmentStringKernel(feats_train, feats_train)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

def poly_match_string ():
	print 'PolyMatchString'

	data=get_dna()
	feats_train=StringCharFeatures(DNA)
	feats_train.set_string_features(data['train'])
	feats_test=StringCharFeatures(DNA)
	feats_test.set_string_features(data['test'])
	degree=3
	inhomogene=False

	kernel=PolyMatchStringKernel(feats_train, feats_train, degree, inhomogene)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

def simple_locality_improved_string ():
	print 'SimpleLocalityImprovedString'

	data=get_dna()
	feats_train=StringCharFeatures(DNA)
	feats_train.set_string_features(data['train'])
	feats_test=StringCharFeatures(DNA)
	feats_test.set_string_features(data['test'])
	length=5
	inner_degree=5
	outer_degree=7

	kernel=SimpleLocalityImprovedStringKernel(
		feats_train, feats_train, length, inner_degree, outer_degree)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

def weighted_degree_string ():
	print 'WeightedDegreeString'

	data=get_dna()
	feats_train=StringCharFeatures(DNA)
	feats_train.set_string_features(data['train'])
	feats_test=StringCharFeatures(DNA)
	feats_test.set_string_features(data['test'])
	degree=20

	kernel=WeightedDegreeStringKernel(feats_train, feats_train, degree)

	#weights=arange(1,degree+1,dtype=double)[::-1]/ \
	#	sum(arange(1,degree+1,dtype=double))
	#kernel.set_wd_weights(weights)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

def weighted_degree_position_string ():
	print 'WeightedDegreePositionString'

	data=get_dna()
	feats_train=StringCharFeatures(DNA)
	feats_train.set_string_features(data['train'])
	feats_test=StringCharFeatures(DNA)
	feats_test.set_string_features(data['test'])
	degree=20

	kernel=WeightedDegreePositionStringKernel(feats_train, feats_train, degree)

	#kernel.set_shifts(zeros(len(data['train'][0]), dtype=int))

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

def locality_improved_string ():
	print 'LocalityImprovedString'

	data=get_dna()
	feats_train=StringCharFeatures(DNA)
	feats_train.set_string_features(data['train'])
	feats_test=StringCharFeatures(DNA)
	feats_test.set_string_features(data['test'])
	length=5
	inner_degree=5
	outer_degree=7

	kernel=LocalityImprovedStringKernel(
		feats_train, feats_train, length, inner_degree, outer_degree)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

###########################################################################
# complex string features
###########################################################################

def comm_word_string ():
	print 'CommWordString'

	data=get_dna()
	order=3
	gap=0
	reverse=False

	charfeat=StringCharFeatures(DNA)
	charfeat.set_string_features(data['train'])
	feats_train=StringWordFeatures(charfeat.get_alphabet())
	feats_train.obtain_from_char(charfeat, order-1, order, gap, reverse)
	preproc=SortWordString()
	preproc.init(feats_train)
	feats_train.add_preproc(preproc)
	feats_train.apply_preproc()

	charfeat=StringCharFeatures(DNA)
	charfeat.set_string_features(data['test'])
	feats_test=StringWordFeatures(charfeat.get_alphabet())
	feats_test.obtain_from_char(charfeat, order-1, order, gap, reverse)
	feats_test.add_preproc(preproc)
	feats_test.apply_preproc()

	use_sign=False
	normalization=FULL_NORMALIZATION

	kernel=CommWordStringKernel(
		feats_train, feats_train, use_sign, normalization)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

def weighted_comm_word_string ():
	print 'WeightedCommWordString'

	data=get_dna()
	order=3
	gap=0
	reverse=False

	charfeat=StringCharFeatures(DNA)
	charfeat.set_string_features(data['train'])
	feats_train=StringWordFeatures(charfeat.get_alphabet())
	feats_train.obtain_from_char(charfeat, order-1, order, gap, reverse)
	preproc=SortWordString()
	preproc.init(feats_train)
	feats_train.add_preproc(preproc)
	feats_train.apply_preproc()

	charfeat=StringCharFeatures(DNA)
	charfeat.set_string_features(data['test'])
	feats_test=StringWordFeatures(charfeat.get_alphabet())
	feats_test.obtain_from_char(charfeat, order-1, order, gap, reverse)
	feats_test.add_preproc(preproc)
	feats_test.apply_preproc()

	use_sign=False
	normalization=FULL_NORMALIZATION

	kernel=WeightedCommWordStringKernel(
		feats_train, feats_train, use_sign, normalization)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

def comm_ulong_string ():
	print 'CommUlongString'

	data=get_dna()
	order=3
	gap=0
	reverse=False

	charfeat=StringCharFeatures(DNA)
	charfeat.set_string_features(data['train'])
	feats_train=StringUlongFeatures(charfeat.get_alphabet())
	feats_train.obtain_from_char(charfeat, order-1, order, gap, reverse)
	preproc=SortUlongString()
	preproc.init(feats_train)
	feats_train.add_preproc(preproc)
	feats_train.apply_preproc()


	charfeat=StringCharFeatures(DNA)
	charfeat.set_string_features(data['test'])
	feats_test=StringUlongFeatures(charfeat.get_alphabet())
	feats_test.obtain_from_char(charfeat, order-1, order, gap, reverse)
	feats_test.add_preproc(preproc)
	feats_test.apply_preproc()

	use_sign=False
	normalization=FULL_NORMALIZATION

	kernel=CommUlongStringKernel(
		feats_train, feats_train, use_sign, normalization)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

###########################################################################
# misc kernels
###########################################################################

def custom ():
	print 'Custom'

	dim=7
	data=rand(dim, dim)
	feats=RealFeatures(data)
	symdata=data+data.T
	lowertriangle=array([symdata[(x,y)] for x in xrange(symdata.shape[1])
		for y in xrange(symdata.shape[0]) if y<=x])

	kernel=CustomKernel(feats, feats)

	kernel.set_triangle_kernel_matrix_from_triangle(lowertriangle)
	km_triangletriangle=kernel.get_kernel_matrix()

	kernel.set_triangle_kernel_matrix_from_full(symdata)
	km_fulltriangle=kernel.get_kernel_matrix()

	kernel.set_full_kernel_matrix_from_full(data)
	km_fullfull=kernel.get_kernel_matrix()

def distance ():
	print 'Distance'

	num_feats=10
	data=rand(num_feats, 9)
	feats_train=RealFeatures(data)
	data=rand(num_feats, 19)
	feats_test=RealFeatures(data)
	width=1.7
	distance=EuclidianDistance()

	kernel=DistanceKernel(feats_train, feats_test, width, distance)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

def auc ():
	print 'AUC'

	num_feats=23
	data=rand(num_feats, 11)
	feats_train=RealFeatures(data)
	data=rand(num_feats, 19)
	feats_test=RealFeatures(data)
	width=1.7
	subkernel=GaussianKernel(feats_train, feats_test, width)

	num_feats=2 # do not change!
	len_train=11
	len_test=17
	data=randint(0, len_train, (num_feats, len_train)).astype(ushort)
	feats_train=WordFeatures(data)
	data=randint(0, len_test, (num_feats, len_test)).astype(ushort)
	feats_test=WordFeatures(data)

	kernel=AUCKernel(feats_train, feats_test, subkernel)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

def combined ():
	print 'Combined'

	kernel=CombinedKernel()
	feats_train=CombinedFeatures()
	feats_test=CombinedFeatures()

	data=get_dna()
	subkfeats_train=StringCharFeatures(DNA)
	subkfeats_train.set_string_features(data['train'])
	subkfeats_test=StringCharFeatures(DNA)
	subkfeats_test.set_string_features(data['test'])
	subkernel=LinearStringKernel(10)
	feats_train.append_feature_obj(subkfeats_train)
	feats_test.append_feature_obj(subkfeats_test)
	kernel.append_kernel(subkernel)

	data=get_dna()
	subkfeats_train=StringCharFeatures(DNA)
	subkfeats_train.set_string_features(data['train'])
	subkfeats_test=StringCharFeatures(DNA)
	subkfeats_test.set_string_features(data['test'])
	degree=3
	subkernel=FixedDegreeStringKernel(10, degree)
	feats_train.append_feature_obj(subkfeats_train)
	feats_test.append_feature_obj(subkfeats_test)
	kernel.append_kernel(subkernel)

	data=get_dna()
	subkfeats_train=StringCharFeatures(DNA)
	subkfeats_train.set_string_features(data['train'])
	subkfeats_test=StringCharFeatures(DNA)
	subkfeats_test.set_string_features(data['test'])
	subkernel=LocalAlignmentStringKernel(10)
	feats_train.append_feature_obj(subkfeats_train)
	feats_test.append_feature_obj(subkfeats_test)
	kernel.append_kernel(subkernel)

	kernel.init(feats_train, feats_train)
	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()

def plugin_estimate ():
	print 'PluginEstimate w/ HistogramWord'

	data=get_dna()
	order=3
	gap=0
	reverse=False

	charfeat=StringCharFeatures(DNA)
	charfeat.set_string_features(data['train'])
	feats_train=StringWordFeatures(charfeat.get_alphabet())
	feats_train.obtain_from_char(charfeat, order-1, order, gap, reverse)

	charfeat=StringCharFeatures(DNA)
	charfeat.set_string_features(data['test'])
	feats_test=StringWordFeatures(charfeat.get_alphabet())
	feats_test.obtain_from_char(charfeat, order-1, order, gap, reverse)

	pie=PluginEstimate()
	lab=rand(feats_train.get_num_vectors()).round()*2-1
	labels=Labels(array(lab))

	pie.train(feats_train, labels)

	kernel=HistogramWordKernel(feats_train, feats_train, pie)
	km_train=kernel.get_kernel_matrix()

	kernel.init(feats_train, feats_test)
	pie.set_testfeatures(feats_test)
	pie.test()
	pie.classify().get_labels()
	km_test=kernel.get_kernel_matrix()

def mindygram ():
	pass

###########################################################################
# call functions
###########################################################################

if __name__=='__main__':
	seed(42)

	linear_byte()

	chi2()
	const()
	diag()
	gaussian()
	gaussian_shift()
	linear()
	poly()
	sigmoid()

	sparse_gaussian()
	sparse_linear()
	sparse_poly()

	linear_word()
	poly_match_word()
	word_match()

	fixed_degree_string()
	linear_string()
	local_alignment_string()
	poly_match_string()
	simple_locality_improved_string()
	weighted_degree_string()
	weighted_degree_position_string()
	locality_improved_string()

	comm_word_string()
	weighted_comm_word_string()
	comm_ulong_string()

	custom()
	distance()
	auc()
	combined()
	plugin_estimate()
	mindygram()
