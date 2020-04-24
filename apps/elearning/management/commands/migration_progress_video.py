from random import weibullvariate

from django.core.management.base import BaseCommand, CommandError
from apps.elearning.models import ProgressVideo


class Command(BaseCommand):
    help = 'Migracion de inscripcion y categoria a progreso de video'

    def add_arguments(self, parser):
        # Optional argument
        parser.add_argument('-i', '--ids', nargs='+', type=int,
                            help='ids de los Progreso de los videos', )

    def handle(self, *args, **options):
        progress_videos = ProgressVideo.objects.filter(id__in=options['ids']) if options[
            'ids'] else ProgressVideo.objects.all()
        for progress_video in progress_videos:
            progress_video.course = progress_video.id_inscription.id_course.title
            progress_video.user = progress_video.id_inscription.id_user.email
            progress_video.category = progress_video.id_category.name
        ProgressVideo.objects.bulk_update(progress_videos,
                                          update_fields=['course', 'user', 'category'])
