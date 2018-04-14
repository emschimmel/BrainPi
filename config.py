file_path               = '../img/'
max_token_time_seconds  = 60            # less is more secure

eigen_trainer_file      = './Data/eigen_trainer.yml'
fisher_trainer_file     = './Data/fisher_trainer.yml'
lbph_trainer_file       = './Data/lbph_trainer.yml'

eigen_data_path         = './Data/lfw_eigen'
fisher_data_path        = './Data/lfw_eigen'
lbph_data_path          = './Data/lfw'

eigen_name_id_file      = './Data/eigen_namedIds.yml'
fisher_name_id_file     = './Data/fisher_namedIds.yml'
lbph_name_id_file       = './Data/lbph_namedIds.yml'

consul_interval         = '30s'
consul_timeout          = '2s'
consul_ip               = '127.0.0.1'
consul_port             = 8500
consul_resolver_port    = 8600

statsd_ip               = 'localhost'
statsd_port             = 8125

redis_service_ip        = 'localhost'
redis_service_port      = 32769
es_service_ip           = 'localhost'
es_service_port         = 32770
mongo_service_ip        = 'localhost'
mongo_service_port      = 27017
rabbit_service_ip       = 'localhost'
rabbit_service_port     = 35672

lightwaveRfIp           = '192.168.0.102'

log_dir                 = '../Logs/'
log_level               = 'DEBUG'

