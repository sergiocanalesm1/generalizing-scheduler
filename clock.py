from apscheduler.schedulers.blocking import BlockingScheduler
import requests

sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon', hour=17)
def scheduled_job():
    r = requests.post("https://generalizing-back-prod.herokuapp.com/api/challenges/")
    print(r.text)


sched.start()
