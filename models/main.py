
from models import m0


def main(json_params = None , model_to = 'message_id'):

        models_resp = []

        #json_params = {'message_id':0,
        #                'dialog_id':0,
        #                'participants_id':0,
        #                'user_id':0,
        #                'content':'test content',
        #                'created_at':111111111,
        #            }

        content = json_params['content']
        to_id = json_params[model_to]

        m0_resp = m0.main(text_message = content , model_to = model_to , to_id = to_id)

        models_resp.append(m0_resp)


        return models_resp



