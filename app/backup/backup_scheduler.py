from apscheduler.schedulers.background import BackgroundScheduler
from app import create_app

scheduler = None

def schedule_backup():
    print("Iniciando programación del respaldo")
    global scheduler

    app = create_app()

    if scheduler:
        scheduler.shutdown()

    from app.services.parametro_service import ParametroService 

    hora_backup_param = ParametroService.get_parametro_by_nombre("Hora_Backup")
    hora_backup = hora_backup_param.valor if hora_backup_param else "02:00"

    # Inicializar el planificador
    scheduler = BackgroundScheduler()
    scheduler.start()

    from app.backup.backup_service import create_backup
    scheduler.add_job(create_backup, 'cron', args=[app], hour=hora_backup.split(':')[0], minute=hora_backup.split(':')[1])

# Verificar los trabajos programados
    list_scheduled_jobs()

def list_scheduled_jobs():
    global scheduler
    if scheduler:
        jobs = scheduler.get_jobs()
        print("Trabajos programados:")
        for job in jobs:
            print(f"ID: {job.id}, Próxima ejecución: {job.next_run_time}, Trigger: {job.trigger}")
    else:
        print("No hay trabajos programados.")