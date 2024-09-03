from dotenv import load_dotenv
from crewai import Crew
from tasks import IdeaValidationTasks 
from agents import IdeaValidationAgents

def main():
    load_dotenv()

    print("## Welcome to the Business Idea validation Crew")
    print('-----------------------------------------------')
    idea = input("What is your idea for a business?: \n")
    market = input("What market do you think this is mainly in?: \n")

    tasks = IdeaValidationTasks()
    agents = IdeaValidationAgents()

    #Create agents
    market_trends_agent = agents.market_trends_agent()
    market_gaps_agent = agents.market_gaps_agent()
    strengths_and_weaknesses_agent = agents.strengths_and_weaknesses_agent()
    opportunities_threats_agent = agents.opportunities_threats_agent()
    financial_analysis_agent = agents.financial_analysis_agent()
    business_validation_agent = agents.business_validation_agent()
    report_agent = agents.report_agent()

    #Create tasks
    market_trends_task = tasks.market_trends_task(market_trends_agent, idea, market)
    market_gaps_task = tasks.market_gaps_task(market_gaps_agent, idea, market)
    strengths_weaknesses_task = tasks.strengths_weaknesses_task(strengths_and_weaknesses_agent, idea, market)
    opportunities_threats_task = tasks.opportunities_threats_task(opportunities_threats_agent, idea, market)
    financial_analysis_task = tasks.financial_analysis_task(financial_analysis_agent, idea, market)
    idea_validation_task = tasks.idea_validation_task(business_validation_agent, idea, market)
    report_writing_task = tasks.report_writing_task(report_agent, idea, market)

    financial_analysis_task.context = [financial_analysis_task, opportunities_threats_task, strengths_weaknesses_task, market_gaps_task, market_trends_task]
    idea_validation_task.context = [opportunities_threats_task, strengths_weaknesses_task, market_gaps_task, market_trends_task]
    report_writing_task.context = [idea_validation_task, financial_analysis_task, opportunities_threats_task, strengths_weaknesses_task, market_gaps_task, market_trends_task]
    
    #Create Crew
    crew = Crew(
        agents = [
            market_trends_agent,
            market_gaps_agent,
            strengths_and_weaknesses_agent,
            opportunities_threats_agent,
            financial_analysis_agent,
            business_validation_agent,
            report_agent
        ],
        tasks = [
            market_trends_task,
            market_gaps_task,
            strengths_weaknesses_task,
            opportunities_threats_task,
            financial_analysis_task,
            idea_validation_task,
            report_writing_task
        ]
    )

    result = crew.kickoff()
    print(result)



if __name__ == '__main__':
    main()