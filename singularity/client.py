import json
import requests

def _response(res):
    try:
        return res.json()
    except:
        return {'error': res.text}

class Client(object):

    def __init__(self, url, insecure=False):
        self.url = url
        self.session = requests.Session()
        self.session.headers = {'Content-Type': 'application/json'}
        if insecure:
            requests.packages.urllib3.disable_warnings()
            self.session.verify = False

    # state api
    def get_state(self):
        url = '{0}/api/state'.format(self.url)
        return _response(self.session.get(url))

    def get_state_underprovisioned(self):
        url = '{0}/api/state/requests/under-provisioned'.format(self.url)
        return _response(self.session.get(url))

    def get_state_overprovisioned(self):
        url = '{0}/api/state/requests/over-provisioned'.format(self.url)
        return _response(self.session.get(url))

    # requests api
    def unpause_request(self, request_id):
        url = '{0}/api/requests/request/{1}/unpause'.format(self.url, request_id)
        return _response(self.session.post(url))

    def run_request(self, request_id):
        url = '{0}/api/requests/request/{1}/run'.format(self.url, request_id)
        return _response(self.session.post(url))

    def pause_request(self, request_id, kill_tasks=False):
        data = {'killTasks': kill_tasks}
        url = '{0}/api/requests/request/{1}/pause'.format(self.url, request_id)
        return _response(self.session.post(url, data=json.dumps(data)))

    def set_instances_request(self, request_id, instances):
        data = {'id': request_id, 'instances': instances}
        url = '{0}/api/requests/request/{1}/instances'.format(self.url, request_id)
        return _response(self.session.put(url, data=json.dumps(data)))

    def bounce_request(self, request_id):
        url = '{0}/api/requests/request/{1}/bounce'.format(self.url, request_id)
        return _response(self.session.post(url))

    def get_request(self, request_id):
        url = '{0}/api/requests/request/{1}'.format(self.url, request_id)
        return _response(self.session.get(url))

    def delete_request(self, request_id):
        url = '{0}/api/requests/request/{1}'.format(self.url, request_id)
        return _response(ctx.obj['session'].delete(url))

    def upsert_request(self, request):
        url = '{0}/api/requests'.format(self.url)
        return _response(self.session.post(url, data=json.dumps(request)))

    def get_requests(self, type):
        if type == 'all':
            url = '{0}/api/requests'.format(self.url)
        elif type in ['pending', 'cleanup']:
            url = '{0}/api/requests/queued/{1}'.format(self.url, type)
        else:
            url = '{0}/api/requests/paused'.format(self.url, type)
        return _response(self.session.get(url))

    # deploys api
    def create_deploy(self, deploy):
        url = '{0}/api/deploys'.format(self.url)
        return _response(session.post(url, data=dumps({'deploy': deploy})))
