
import consul
import sys
sys.path.append('../')
import config

def main():
    c = consul.Consul()

    # Register Service
    c.agent.service.register('Eye Pi',
                             address=config.eye_pi_ip,
                             service_id='eye_pi',
                             port=config.eye_pi_port,
                             tags=['LOGIN'],
                             check={'script': 'ps | awk -F" " \'/PythonEyePiServer.py/ && !/awk/{print $1}\'',
                                    'id': 'eye_pi', 'name': 'eye_pi process tree check', 'Interval': '10s',
                                    'timeout': '2s'})
    c.agent.service.register('Face Pi',
                             address=config.face_pi_ip,
                             service_id='face_pi',
                             port=config.face_pi_port,
                             tags=['LOGIN'],
                             check={'script': 'ps | awk -F" " \'/PythonFacePiServer.py/ && !/awk/{print $1}\'',
                                    'id': 'eye_pi', 'name': 'face_pi process tree check', 'Interval': '10s',
                                    'timeout': '2s'})
    c.agent.service.register('Weather Pi',
                             address=config.weather_pi_ip,
                             service_id='weather_pi',
                             port=config.weather_pi_port,
                             tags=['WEATHER'],
                             check={'script': 'ps | awk -F" " \'/PythonWeatherPiServer.py/ && !/awk/{print $1}\'',
                                    'id': 'eye_pi', 'name': 'weather_pi process tree check', 'Interval': '10s',
                                    'timeout': '2s'})
    c.agent.service.register('Music Pi',
                             address=config.music_pi_ip,
                             service_id='music_pi',
                             port=config.music_pi_port,
                             tags=['MUSIC'],
                             check={'script': 'ps | awk -F" " \'/PythonMusicPiServer.py/ && !/awk/{print $1}\'',
                                    'id': 'eye_pi', 'name': 'music_pi process tree check', 'Interval': '10s',
                                    'timeout': '2s'})
    c.agent.service.register('Agenda Pi',
                             address=config.agenda_pi_ip,
                             service_id='agenda_pi',
                             port=config.agenda_pi_port,
                             tags=['AGENDA'],
                             check={'script': 'ps | awk -F" " \'/PythonAgendaPiServer.py/ && !/awk/{print $1}\'',
                                    'id': 'eye_pi', 'name': 'agenda_pi process tree check', 'Interval': '10s',
                                    'timeout': '2s'})
    c.agent.service.register('Home Pi',
                             address=config.kaku_pi_ip,
                             service_id='kaku_pi',
                             port=config.kaku_pi_port,
                             tags=['KAKU'],
                             check={'script': 'ps | awk -F" " \'/PythonHomePiServer.py/ && !/awk/{print $1}\'',
                                    'id': 'eye_pi', 'name': 'home_pi process tree check', 'Interval': '10s',
                                    'timeout': '2s'})
    c.agent.service.register('Short Term Memory',
                             address=config.short_storage_ip,
                             service_id='short_term_memory',
                             port=config.short_storage_port,
                             tags=['DATA'],
                             check={'script': 'ps | awk -F" " \'/ShortTermMemoryServer.py/ && !/awk/{print $1}\'',
                                    'id': 'eye_pi', 'name': 'short_term_memory process tree check', 'Interval': '10s',
                                    'timeout': '2s'})
    c.agent.service.register('Long Term Memory',
                             address=config.long_storage_ip,
                             service_id='long_term_memory',
                             port=config.long_storage_port,
                             tags=['DATA'],
                             check={'script': 'ps | awk -F" " \'/LongTermMemoryServer.py/ && !/awk/{print $1}\'',
                                    'id': 'eye_pi', 'name': 'long_term_memory process tree check', 'Interval': '10s',
                                    'timeout': '2s'})

    # List all registered Services
    for x in c.agent.services():
        print(x)

        # To remove the service entry
        # c.agent.service.deregister(service_id='my_http_service_1')


if __name__ == "__main__":
    main()