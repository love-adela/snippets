@dag(default_args=DEFAULT_ARGS, schedule_interval=None, start_date=days_ago(2), tags=['example'])
def example_dag_decorator(email: str = 'love.adelar@gmail.com'):
    """
    DAG to send server IP to email

    :param email: Email to send IP to. Defaults to love.adelar@gmail.com.
    :type email: str
    """

    get_ip = GetRequestOperator(task_id='get_ip', url="http://httpbin.org/get")

    @task(multiple_outputs=True)
    def prepare_email(raw_json: Dict[str, Any]) -> Dict[str, str]:
        external_ip = raw_json['origin']
        return {
            'subject': f'Server connected from {external_ip}',
            'body': f'Seems like today your server executing Airflow is connected from IP {external_ip}<br>',
        }

    email_info = prepare_email(get_ip.output)

    EmailOperator(
        task_id='send_email', to=email, subject=email_info['subject'], html_content=email_info['body']
    )
dag = example_dag_decorator()
