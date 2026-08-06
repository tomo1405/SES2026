import pytest
from src_0081 import task_func

def test_task_func():
    template_folder = "templates"
    app = task_func(template_folder)
    assert app.template_folder == template_folder

    @app.route('/', methods=['POST'])
    def handle_post():
        data = request.get_json()
        logging.info(json.dumps(data))
        return render_template('index.html', data=data)

    with app.test_client() as client:
        response = client.post('/', data=json.dumps({"key": "value"}), content_type='application/json')
        assert response.status_code == 200
        assert response.data == b'{"key": "value"}'