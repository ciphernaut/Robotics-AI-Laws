import unittest
from law_testing_framework.llm_client import query_llm

class TestLLMCapabilities(unittest.TestCase):

    def test_basic_reasoning(self):
        """
        Tests the LLM's ability to perform a simple reasoning task.
        """
        prompt = "If a train travels at 60 mph, how long does it take to travel 60 miles?"
        response = query_llm(prompt)
        self.assertIn("1 hour", response.lower())

    def test_code_generation(self):
        """
        Tests the LLM's ability to generate code.
        """
        # This would involve querying the LLM and asserting the response.
        # For now, we'll just pass.
        pass

if __name__ == "__main__":
    unittest.main()

