from sample import Sampler
experiment_name = 'ForwardRNN_512'
s = Sampler(experiment_name)
s.sample(N=1000000, stor_dir='../evaluation', T=0.7, fold=[1], epoch=[9], valid=True, novel=True, unique=True, write_csv=True)
#csv stored in ./evaluation/ForwardRNN_512/molecules/