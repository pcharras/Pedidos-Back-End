from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from app.services.email_service import EmailService
import os

email_api_blueprint = Blueprint('email_api', __name__)
api = Api(email_api_blueprint)

class EmailResource(Resource):
    def post(self):
        sender_email = request.form.get('sender_email')
        receiver_email = request.form.get('receiver_email')
        subject = request.form.get('subject')
        body = request.form.get('body')
        print("quien envia",sender_email,"para quien",receiver_email,"titulo",subject,"mesaje",body)
        if 'file' not in request.files:
            return {'error': 'No file part'}, 400

        file = request.files['file']
        print("archivo antes de servicio",file)
        if file.filename == '':
            return {'error': 'No selected file'}, 400

        file_path = os.path.join('uploads', file.filename)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        file.save(file_path)
        print("archivo path antes de servicio",file_path)
        success, message = EmailService.send_email_with_attachment(
            sender_email, receiver_email, subject, body, file_path
        )

        os.remove(file_path)
        if success:
            return {'message': message}, 200
        else:
            return {'error': message}, 500

api.add_resource(EmailResource, '/send_excel')
