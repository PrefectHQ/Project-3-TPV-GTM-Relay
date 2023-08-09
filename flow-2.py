from prefect import flow, task
import marvin
from typing import List


@ai_fn
@task
def resource_content(text: str) -> str:
     """Given input text, suggest relevant Prefect resources based on the content of text""" 

@flow
def main_flow(text: str):
   if not text:
       resource_content("Hi I'm Rob, I'd like to learn how Prefect integrates with ECS")
   return resource_content(text)

if __name__ == "__main__":
    main_flow()
