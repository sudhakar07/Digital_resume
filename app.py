from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Sudhakar_Lead_Consultant_Resume.pdf"
profile_pic = current_dir / "assets" / "1615946600759.jpg"
profile_vid = current_dir / "assets" / "Self_intro.mp4"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Sudhakar Govindaraj"
PAGE_ICON = ":wave:"
NAME = "Sudhakar Govindaraj"
DESCRIPTION = """
WorkFusion Solution Designer, Business process design, develops, and implements automation solutions using WorkFusion's intelligent automation platform, leveraging RPA, AI, and machine learning technologies to enhance business processes and increase efficiency."""
EMAIL = "sudhakargk74@gmail.com"
mobile = "+91- 9894045556"
SOCIAL_MEDIA = {
    "Medium": "https://medium.com/@sudhakargk74",
    "LinkedIn": "https://www.linkedin.com/in/sudhakar-govindaraj-74107669/",
   # "GitHub": "https://github.com",
   # "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Application FAQs intelligence": "-1st  Place",
    "🏆 Chatbots in customer service ": "-2nd Place",
    "🏆 Passport PII extraction IDP": "http://extract-mrz-app.herokuapp.com",
    
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2)
with col1:
    st.image(profile_pic, width=200)
    st.write("📫", EMAIL)
    st.write(":iphone:", mobile)



with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    agree = st.checkbox('Play for Self Intro')
    if agree:
        video_file = open(profile_vid, 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
    
    


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"Social Media : [{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write("---")
st.write(
    """
- ✔️ Overall 13+ years of IT experience. A Lead Consultant with over 7+ years of experience in Machine learning, AI, Data scientist, RPA, UiPath and different RPA tools.
- ✔️ 5+ years of experience developing applications using Java/J2EE technologies in Insurance and Healthcare domains.
- ✔️ Extensive experience in Cognitive Business Process Development with the focus in Banking, Insurance, and Health care.
- ✔️ End-to-End ML & RPA life cycle design and development expertise using WorkFusion Machine Learning ODF,  AutoML -SDK, OCR, SPA, RPA, and Uipath.
- ✔️ Implemented processes that monitor emails, download pdf documents, perform OCR, and tag data by Machine Learning models and upload them to LLEs, this reduced manual document handling errors and handling time by 90%.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write("---")
st.info(
    """
✔️WorkFusion					\t\t\t\t\t:	ML, ODF, Control Tower, Scheduler, SPA Studio, RPA, Workspace, Mesos, Marathon, Nexus, Amazon S3, ML-SDK\n
✔️Languages					\t\t\t\t\t:	Java , Python                                                                                           \n
✔️Machine Learning & AI		\t\t\t\t\t:	SciKit Learn, NLP, Streamlit                                                                            \n
✔️Data Visualization 			\t\t\t\t\t:	Matplotlib and Seaborn                                                                                  \n
✔️Data Mining					\t\t\t\t\t:	Pandas, Numpy                                                                                           \n
✔️BI							\t\t\t\t\t:	Tableau, Kibana ELK, Power BI                                                                                    \n
✔️RPA Tool					\t\t\t\t\t:	Workfusion RPA, UiPath , Selenium                                                                       \n
✔️Web Technologies			\t\t\t\t\t:	HTML, JSP, Servlet, JavaScript, Ajax, JQuery ,XML,XSLT                                                  \n
✔️RDBMS						\t\t\t\t\t:	Oracle,MYSQL                                                                                            \n
✔️Database Connectivity		\t\t\t\t\t:	JDBC, Spring JDBC Templates,  ORM                                                                       \n
✔️Frameworks					\t\t\t\t\t:	Struts, Hibernate, Liferay, Spring                                                                      \n
✔️Tools/IDE					\t\t\t\t\t:	Workfusion Studio Eclipse, Net beans , TOAD, Mail Server, Log4j                                         \n
✔️Application Server			\t\t\t\t\t:	BEA Web Logic10.3,Websphere                                                                             \n
✔️Web Server					\t\t\t\t\t:	WebSphere Portal, Apache tomcat                                                                         \n
✔️Operating Systems			\t\t\t\t\t:	Windows, Linux(UBUNTU)                                                                                  \n
✔️Configuration Tools			\t\t\t\t\t:	GIT, SVN, Mercurial                                                                                     \n
✔️Testing Tools				\t\t\t\t\t:	Mockito-junit , Code Coverage                                                                           \n
✔️CI / CD						\t\t\t\t\t:	Jenkins, Sonar                                                                                          \n
                                                                                                                                                \n

"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Lead Consultant | Infosys Limited, Chennai**")
st.write("11/2018 - Present")
#st.write(
#    """
#- ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
#- ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
#- ► Redesigned data model through iterations that improved predictions by 12%
#"""
#)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Senior Associate | Cognizant Technology Solutions, Chennai**")
st.write("Oct 2015  - Nov 2018 ")
#st.write(
#    """
#- ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
#- ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
#- ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
#"""
#)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Senior software Engineer | Xerago E-Biz Services Pvt. Ltd, Chennai**")
st.write("Dec 2011 - Oct 2015")
#st.write(
#    """
#- ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
#- ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
#- ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
#"""
#)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"{project} ({link})")



st.write('\n')
st.subheader("Certification")
st.write("---")
st.info(
    """
✔️ Workfusion :                                                    \n
	✔️ ODF2.0 -Open Development Framework                          \n
	✔️ Digital Worker                                              \n
	✔️ Intelligent Automation for Banking                          \n
	✔️ WorkFusion ML Engineer                                      \n
	✔️ Machine Learning Data Analyst                               \n
	✔️ ELK Elasticsearch with Logstash and Kibana                  \n
	✔️ RPA Core                                                    \n
✔️ Python :                                                        \n
	✔️ Python for Data Science and machine learning                \n
	✔️ NLP - Natural Language Processing with Python               \n
	✔️ Building Machine Learning Web Apps with Streamlit           \n
                                                                   \n
✔️ UiPath RPA Developer Advanced Diploma                           \n
✔️ UiPath RPA Solution Architect - Completion Diploma              \n
✔️ AA- Automation Anywhere Certified Advanced RPA Professional     \n
✔️ Hibernate and JPA with spring boot                              \n
                                                                   \n
"""
)


st.write('\n')


st.header(":mailbox: Get In Touch With Me!")
st.write("---")


contact_form = """
<form action="https://formsubmit.co/94bdffa1516793e9eeb6b6010eaa07cb" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("styles/style.css")
