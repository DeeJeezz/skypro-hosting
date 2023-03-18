from typing import Dict, List, Tuple, Union

from flask import Blueprint, Response, jsonify, request
from marshmallow import ValidationError
from sqlalchemy import text

from builder import build_query
from db import db
from models import BatchRequestSchema

main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query() -> Union[Response, Tuple[Response, int]]:
    # TODO: Принять запрос от пользователя
    data: Dict[str, Union[List[dict], str]] = request.json
    # TODO: Обработать запрос, валидировать значения
    try:
        validated_data = BatchRequestSchema().load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400
    # TODO: Выполнить запрос
    result = None
    for query in validated_data['queries']:
        result = build_query(
            cmd=query['cmd'],
            value=query['value'],
            file_name=validated_data['file_name'],
            data=result,
        )

    return jsonify(result)


@main_bp.route('/ping', methods=['GET'])
def ping():
    return 'pong'


@main_bp.route('/test_db', methods=['GET'])
def test_db():
    result = db.session.execute(
        text(
            'SELECT 1'
        )
    ).scalar()

    return jsonify(
        {
            'result': result,
        }
    )
