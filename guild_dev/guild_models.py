# coding: utf-8
"""
A collection of classes representing the tables in the "Guild_2.db" datadb.Model

"""
from guild_dev import db
from datetime import datetime



class Committee(db.Model):
    """
    Class Committee:
        A class containing details on an individual Member's Committee assignments
        represents a row in the *committees* table

    """
    __tablename__ = 'committees'

    id = db.Column(db.ForeignKey('members.id'), primary_key=True, nullable=False)
    member_year = db.Column(db.Integer, primary_key=True, nullable=False)
    hospitality = db.Column(db.Boolean)
    hosp_prefs = db.Column(db.Text)
    audience_services = db.Column(db.Boolean)
    greeter = db.Column(db.Boolean)
    floater = db.Column(db.Boolean)
    chester = db.Column(db.Boolean)
    chester_avail = db.Column(db.Text)
    transportation = db.Column(db.Boolean)
    weekdays = db.Column(db.Text)
    weekends = db.Column(db.Text)
    tours = db.Column(db.Boolean)
    flower = db.Column(db.Boolean)
    flower_prefs = db.Column(db.Text)
    library = db.Column(db.Boolean)
    office_rescue = db.Column(db.Boolean)
    student = db.Column(db.Boolean)
    created_on = db.Column(db.DateTime, default=datetime.date())
    updated_on = db.Column(db.DateTime,default=datetime.utcnow, updated_on=datetime.utcnow)

    committee_members = db.relationship('Member', backref='opts', lazy=True)


class ExcludePerAmy(db.Model):
    """
    Class ExcludePerAmy:
        A class containing list of Membersid's no longer in the Guild
        represents a row in the *exclude_per_amy* table

    """
    __tablename__ = 'exclude_per_amy'

    id = db.Column(db.Integer, primary_key=True)
    removal_date = db.Column(db.DateTime)
    reason = db.Column(db.Text)
    comment = db.Column(db.Text)


class Finance(db.Model):
    """
        Class Finance:
            A class containing details on an individual Member's Dues/Donation arrangements
            represents a row in the *finance* table

        """
    __tablename__ = 'finance'

    id = db.Column(db.ForeignKey('members.id'), primary_key=True, nullable=False)
    member_year = db.Column(db.Integer, primary_key=True, nullable=False)
    renew_date = db.Column(db.DateTime)
    dues = db.Column(db.Float)
    donation = db.Column(db.Float)
    donor_only = db.Column(db.Boolean)
    family = db.Column(db.Boolean)
    payment_method = db.Column(db.Text)
    created_on = db.Column(db.DateTime, default=datetime.date())
    updated_on = db.Column(db.DateTime, default=datetime.utcnow, updated_on=datetime.utcnow)

    finance_members = db.relationship('Member', backref='mfin', lazy=True)


class MemberRelate(db.Model):
    """
        Class MemberRelate:
            A associatin class relating  individual 8Family" Member's relationship
            represents a row in the *member_relate* table

        """
    __tablename__ = 'member_relate'

    primary_id = db.Column(db.Integer, primary_key=True, nullable=False)
    related_id = db.Column(db.Integer, primary_key=True, nullable=False)
    relationship = db.Column(db.Text)
    created_on = db.Column(db.DateTime, default=datetime.date())
    updated_on = db.Column(db.DateTime, default=datetime.utcnow, updated_on=datetime.utcnow)


class Member(db.Model):
    """
        Class Member:
        A class containing details on an individual Member
        represents a row in the *members* table

        *mbr_committees* is a related attribute of the embedded Committee object specified by the relationship
        specification. *mbr_finance* is a related attribute of the embedded Finance object specified by the
        relationship specification.

        the relationship specifications are db.Modeld on:
        'https://docs.google.com/document/d/1-qI2OF2ovuK_AxIiJk12gveQVRo3aFOprecq0j9Cj-o/edit#heading=h.820c1e46t1rx'
        """
    __tablename__ = 'members'

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.Integer)
    last_name = db.Column(db.Text)
    first_name = db.Column(db.Text)
    street_address = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    zip_code = db.Column(db.Text)
    telephone = db.Column(db.Text)
    cell_phone = db.Column(db.Text)
    email_address = db.Column(db.Text)
    image_file_link = db.Column(db.Text)
    new = db.Column(db.Text)
    enroled = db.Column(db.DateTime)
    member_since = db.Column(db.Integer)
    created_on = db.Column(db.DateTime, default=datetime.date())
    updated_on = db.Column(db.DateTime, default=datetime.utcnow, updated_on=datetime.utcnow)

    mbr_committees = db.relationship('Committee',
                                     primaryjoin="and_(Committee.id==Member.id, Committee.member_year==2019)",
                                     backref='mbr')
    mbr_finance = db.relationship('Finance', primaryjoin="and_(Finance.id==Member.id, Finance.member_year==2019)",
                                  backref='fin')
    mbr_role = db.relationship('Role', backref='mrole', lazy=True)

    @property
    def full_name(self):
        return f"{self.first_name.strip()} {self.last_name}"

    def __repr__(self):
        return "Member Class object specified by: session.query(Member).filter_by(id=??).first()"

    def __str__(self):
        return f"Members(FullName = '{self.full_name}',id='{self.id}',  EmailAddress='{self.email_address}'"


class Role(db.Model):
    """
        Class Role:
            A class containing details on Roles that Members can be assigned
            represents a row in the *role* table

        """
    __tablename__ = 'role'

    role_id = db.Column(db.ForeignKey(Member.role), primary_key=True)
    role = db.Column(db.Text)
    created_on = db.Column(db.DateTime, default=datetime.date())

