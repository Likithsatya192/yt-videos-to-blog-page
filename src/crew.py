from crewai import Crew, Process
from agents import blog_writer, blog_researcher
from tasks import research_task, writer_task

crew = Crew(
    agents=[blog_researcher,blog_writer],
    tasks=[research_task, writer_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    share_crew=True,
    max_rpm=100
)

result = crew.kickoff(inputs={"topic":"AI VS ML VS DL vs Data Science"})
print(result)