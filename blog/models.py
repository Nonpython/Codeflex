from django.db import models
from mailinglist.models import MailingList
from markupfield.fields import MarkupField


class User(models.Model):
    # General:
    userid                  = models.AutoField(primary_key=True, unique=True)
    username                = models.CharField(maxlength=40, unique=True)
    firstname               = models.CharField(maxlength=40)
    lastname                = models.CharField(maxlength=40)
    email                   = models.CharField(maxlength=100)
    canAccessAdmin          = models.BooleanField(default=False)
    # Blog:
    canCommentToBlog        = models.BooleanField(default=True)
    canMakeBlogPost         = models.BooleanField(default=False)
    canEditOthersBlogPost   = models.BooleanField(default=False)
    canModerateBlogComments = models.BooleanField(default=False)
    # Forum:
    canMakeForumPost        = models.BooleanField(default=True)
    canModerateForum        = models.BooleanField(default=False)
    # Bugtracker:
    canCreateIssue          = models.BooleanField(default=True)
    canModerateBugTracker   = models.BooleanField(default=False)
    canTakeOwnershipOfBug   = models.BooleanField(default=False)
    # Wiki:
    canEditWikiPage         = models.BooleanField(default=True)
    canCreateWikiPage       = models.BooleanField(default=True)
    canDeleteWikiPage       = models.BooleanField(default=False)
    # This may be counterintuitive to those that are used to Unix based
    # systems, but 0 is the least privilage level, not the highest.
    WikiClearanceGroup      = models.IntField(default=0)
    # Mailinglist:
    subscribedLists         = models.ManyToManyField(MailingList)


class Post(models.Model):
    creator         = models.ForeignKey(Users)
    lastEditor      = models.ForeignKey(Users)
    createdTime     = models.DateTimeField(auto_now_add=True)
    lastChangedTime = models.DateTimeField(auto_now=True)
    postText        = MarkupField(markup_type='markdown')
