from flask import url_for

from informatics_front.view.course.monitor.monitor import WorkshopMonitorApi


# def test_get_problems(ongoing_workshop):
#     workshop = ongoing_workshop['workshop']
#
#     result = WorkshopMonitorApi._extract_problem_ids(workshop.id)
#
#     problems = ongoing_workshop['contest'].statement.problems
#     problem_ids = list(p.id for p in problems)
#
#     assert set(problem_ids) == set(result)
#
#
# def test_get_users(applied_workshop_connection):
#     workshop = applied_workshop_connection.workshop
#
#     users = WorkshopMonitorApi._find_users_on_workshop(workshop.id)
#
#     assert users == [applied_workshop_connection.user_id]


def test_simple_view(client, monitor, accepted_workshop_connection):
    workshop = accepted_workshop_connection.workshop
    url = url_for('monitor.workshop', workshop_id=workshop.id)
    resp = client.get(url)
    assert resp.status_code == 200