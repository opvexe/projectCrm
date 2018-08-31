from django.db import models


# Create your models here.

# 创建表结构
class Customer(models.Model):
    '''客户信息'''
    # blank=True 该表可以为空，null=True 数据库该字段可以为空 ；； === 非重要性字段 成对出现
    name = models.CharField(max_length=32, blank=True, null=True)
    qq = models.CharField(max_length=64, unique=True)
    qq_name = models.CharField(max_length=32, blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    souce_choice = ((0, '转介绍'),
                    (1, 'QQ'),
                    (2, '官网'),
                    (3, '百度推广'),
                    (4, '知乎'),
                    (5, '市场推广'),
                    )
    souce = models.SmallIntegerField(choices=souce_choice)
    referral_from = models.CharField(verbose_name='转介绍人', max_length=64, blank=True, null=True)

    consult_course = models.ForeignKey('Course', verbose_name='咨询课程')  # 对应课程表
    content = models.CharField(verbose_name='咨询详情')
    consultant = models.ForeignKey('UserProfile')
    memo = models.CharField(blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', blank=True, null=True)

    def __str__(self):
        return self.qq


class Tag(models.Model):
    '''标签表'''
    name = models.CharField(unique=True)

    def __str__(self):
        return self.name


class CustomerFollowUp(models.Model):
    ''''客户跟进表'''
    customer = models.ForeignKey('Customer')
    content = models.CharField(verbose_name='跟进内容')
    consultant = models.ForeignKey('UserProfile')
    date = models.DateTimeField(auto_now=True)
    intention_choices = ((0, '2周内报名'),
                         (1, '一个月内报名'),
                         (2, '近期无报名计划'),
                         (3, '已在其他报名'),
                         (4, '已拉黑'),
                         )
    intention = models.SmallIntegerField(choices=intention_choices)

    def __str__(self):
        return '<%s : %s>' % (self.customer, self.intention)


# 课程与班级关系 ,课程1对多Forgein
class Course(models.Model):
    '''课程表'''
    name = models.CharField(max_length=64, unique=True)
    price = models.PositiveIntegerField()  # PositiveIntegerField   正整数
    period = models.PositiveIntegerField(verbose_name='周期(月)')  # 周期
    outline = models.TextField()  # 大文本。默认对应的form标签是textarea。

    def __str__(self):
        return self.name


class Branch(models.Model):
    '''校区'''
    name = models.CharField(max_length=128, unique=True)
    address = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class ClassList(models.Model):
    '''班级表'''
    course = models.ForeignKey('Course')
    semester = models.PositiveSmallIntegerField(verbose_name='学期')
    teacher = models.ManyToManyField('UserProfile')
    branch = models.ForeignKey('Branch')
    class_type_choice = ((0, '面授（脱产）'),
                         (1, '面授（周末）'),
                         (2, '网络班'),
                         )
    class_type = models.SmallIntegerField(choices=class_type_choice)
    start_data = models.DateField(verbose_name='开班日期')
    end_data = models.DateField(verbose_name='结束日期', blank=True, null=True)

    def __str__(self):
        return '%s %s %s' %(self.branch,self.course,self.semester)


class CourseRecord(models.Model):
    '''课程记录表'''
    pass


# 报名的则为学生，没报名则为客户
class Enrolment(models.Model):
    '''报名表'''
    pass


class UserProfile(models.Model):
    '''账户表'''
    pass


class Role(models.Model):
    '''角色表'''
    pass
