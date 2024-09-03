from textwrap import dedent
from crewai import Task

class IdeaValidationTasks():
    def market_trends_task(self, agent, idea, market):
        return Task(
            description=dedent(f"""\
                Your task is to guide me in identifying and analyzing current trends 
                in the market to determine the viability and potential success of a 
                business idea. I need insights into the latest market trends, consumer 
                preferences, emerging technologies, and any other relevant factors that 
                could impact the success of a new venture.

                Idea: {idea}
                Market: {market}"""),
                expected_output=dedent("""\
                A detailed report summarizing key findings about each trend that impacts 
                the idea, highlighting information that could be relevant for the 
                improvement/viability of the idea."""),
                async_execution=True,
                agent=agent,
                #human_input=True
            )
    
    def market_gaps_task(self, agent, idea, market):
        return Task(
            description=dedent(f"""\
                Your task is to leverage your expertise and help identify potential 
                gaps in the market to point out aspects of a specific business idea. 
                The goal is to provide strategic insights that can guide the development 
                and execution of the business concept effectively.

                Idea: {idea}
                Market: {market}"""),
                expected_output=dedent("""\
                A report on potential market gaps considering:
                Target Market: __
                Unique Value Proposition: __
                Ensure that your analysis is comprehensive, data-driven, and tailored 
                to the specific business idea provided. Focus on outlining actionable 
                recommendations and highlighting key opportunities that align with the 
                business's objectives.
                Examples to guide your analysis: Conducting in-depth market research, 
                utilizing competitive analysis tools, studying consumer demographics 
                and preferences based on data-driven insights."""),
                async_execution=True,
                agent=agent
            )
    
    def strengths_weaknesses_task(self, agent, idea, market):
        return Task(
            description=dedent(f"""\
                Your task is to conduct a thorough analysis of a company's strengths 
                and weaknesses. Please provide the following details for the company 
                you want to evaluate:
                Company Name: __
                Industry: __
                Key Competitors: __
                Market Position: __
                Financial Performance: __
                Keep in mind that you need to delve into various aspects such as 
                financial health, market share, competitive advantages, management team, 
                operational efficiency. Your report 
                should offer a comprehensive overview that highlights both positive 
                attributes and areas for improvement.

                Idea: {idea}
                Market: {market}"""),
                expected_output=dedent("""\
                For strengths, focus on unique selling propositions, successful strategies, 
                loyal customer base, strong brand reputation, talented workforce, and 
                innovative products/services. For weaknesses, address areas like financial 
                vulnerabilities, outdated technology, poor market positioning, legal or 
                regulatory issues, high employee turnover, or any other relevant challenges.

                For example, you might assess a tech startup's strengths in disruptive 
                technology, agile development, and visionary leadership, combined with 
                weaknesses in market penetration, limited funding, and scalability risks."""),
                async_execution=True,
                agent=agent
            )
    
    def opportunities_threats_task(self, agent, idea, market):
        return Task(
            description=dedent(f"""\
                Analyzing the market requires a keen understanding of industry trends, 
                consumer behaviors, competitive landscape, and potential regulatory 
                changes. Begin by conducting comprehensive research on the market segment, 
                identifying key players, market size, growth projections, and any recent 
                developments. Next, assess the opportunities present in the market. Highlight 
                emerging trends, untapped customer segments, technological advancements, or 
                any other factors that could benefit the proposed business idea. Provide 
                detailed insights on how the business can leverage these opportunities for 
                growth and success. Moving on to threats, identify potential challenges that 
                the business might face. This could include market saturation, changing 
                consumer preferences, increasing competition, or external factors like economic 
                downturns or regulatory hurdles. Suggest strategies to mitigate these threats 
                and strengthen the business's position in the market.
                               
                Idea: {idea}
                Market: {market}"""),
                expected_output=dedent("""\
                In your report, ensure to present data-driven insights, actionable 
                recommendations, and a clear assessment of the market dynamics. Your analysis 
                should help validate the feasibility of the proposed business idea and guide 
                decision-making processes for the stakeholders involved."""),
                async_execution=True,
                agent=agent
            )
    
    def financial_analysis_task(self, agent, idea, market):
        return Task(
            description=dedent(f"""\
                Your task is to analyze the monetization potential and financial viability 
                of the provided business idea. The goal is to generate a comprehensive 
                financial analysis report highlighting potential monetization strategies and 
                avenues for financial success.

                Idea: {idea}
                Market: {market}"""),
                expected_output=dedent("""\
                    Keep in mind the need for detailed market research, a thorough evaluation 
                    of revenue streams, cost analysis, competitor benchmarking, and a clear 
                    roadmap for financial sustainability. Focus on outlining the key financial 
                    metrics, profit projections, investment requirements, and potential risks 
                    associated with the monetization strategies proposed. For example, you would 
                    evaluate the pricing model, customer acquisition costs, and lifetime value 
                    of customers to determine the long-term profitability of the business idea. 
                    Additionally, you would explore alternative revenue sources, partnerships, 
                    and scalability options to enhance the overall financial outlook of the 
                    venture."""),
                agent=agent
            )
    
    def idea_validation_task(self, agent, idea, market):
        return Task(
            description=dedent(f"""\
                Your task is to assess the viability of a business idea based on the 
                provided market analysis information. Evaluate the market need, competition, 
                target audience, and feasibility of the idea to deliver a comprehensive 
                validation report for the client. Please consider factors such as market 
                trends, customer demographics, competitive landscape, potential barriers 
                to entry, and the unique value proposition of the business idea when analyzing 
                its viability. Your goal is to provide a detailed report outlining the strengths,
                weaknesses, opportunities, and threats associated with the proposed business 
                concept.

                Idea: {idea}
                Market: {market}"""),
                expected_output=dedent("""\
                    after reviewing the market analysis data, you will analyze the target 
                    market's size and growth potential, identify key competitors and their 
                    market share, evaluate the demand for the product or service, and assess 
                    the overall feasibility of the business idea. Your report should include 
                    actionable insights and strategic recommendations to help the client make 
                    informed decisions about moving forward with the venture."""),
                memory=True,
                agent=agent
            )
    
    def report_writing_task(self, agent, idea, market):
        return Task(
            description=dedent(f"""\
                Compile all the research findings, industry analysis, and strategic 
                talking points into a comprehensive report for 
                the client.
                Ensure the report is detailed and equips the client with all 
                the necessary information and strategies.
                               
                Idea: {idea}
                Market: {market}"""),
            expected_output=dedent(f"""\
                A well-structured and incredibly well formatted report that includes sections for Introduction, 
                Industry Insight, PESTEL Analysis, Porter's Five Forces Analysis, 
                CATWOE Analysis, Business Strategies, Business Frameworks, Requirement 
                Analysis, Revenue Streams, Marketing Strategy, Slogans, Tweets, 
                Marketing Channels, Unique selling points, Path to an MVP, Customer persona, 
                Finances, go-to-market strategy, competitive analysis, and overal idea 
                validation."""),
            agent=agent
        )
                