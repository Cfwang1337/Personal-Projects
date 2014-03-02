class Institution:
    publications = []
    def __init__(self,name,political_alignment,publications):
        self.name = name
        self.political_alignment = political_alignment
        self.publications = publications

class Publication(Institution):
    def publish(self,title,author,subject,date,url):
        publication_dict = dict(
            title = title,
            author = author,
            subject = subject,
            date = date,
            url = url)
        print publication_dict
        #self.assertEqual(True, isinstance(title,basestring))
        self.publications.append(publication_dict)


'''
2014-02-21 Frederick M. Hess . Common Core: Teachers unions think again American Enterprise Institute
2014-02-21 Jonah Goldberg. Attacking diversity of thought American Enterprise Institute
2014-02-20 Andrew P. Kelly . Obamas college ratings plan is just more of the same American Enterprise Institute
2014-02-14 Andrew P. Kelly. The college-readiness kerfuffle American Enterprise Institute
2014-02-14 Michael Q. McShane. De Blasio cracks down on education reform American Enterprise Institute
2014-02-14 Frederick M. Hess . Focus on the opportunities ed tech brings, not the hype American Enterprise Institute
'''

thinktank = Institution("American Enterprise Institute","Conservative",[])
print thinktank.name
print thinktank.political_alignment

publication = Publication(thinktank.name,thinktank.political_alignment,thinktank.publications)
publication.publish("Common Core: Teachers unions think again","Frederick M. Hess","Education","2014-02-21","http://www.aei.org/article/education/k-12/system-reform/common-core-teachers-unions-think-again/")

publication.publish("Attacking diversity of thought","Jonah Goldberg", "Education","2014-02-21","http://www.aei.org/article/education/k-12/system-reform/common-core-teachers-unions-think-again/")

#Universe("American Enterprise Institute")

#print american_enterprise_institute.publications
print len(publication.publications)
