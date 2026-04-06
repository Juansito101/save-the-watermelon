
Test Game Logic:



1. def test_get_word_returns_uppercase(self):
        """Test that get_word returns a string in uppercase"""
        word = get_word()
        self.assertTrue(word.isupper())



2. def test_get_word_is_string(self):
        """Test that get_word returns a string"""
        word = get_word()
        self.assertIsInstance(word, str)

3.  def test_mask_word_length(self):
        """Masked word should have same length as original"""
        word = "SNAREDRUM"
        masked = mask_word(word, reveal_count=2)
        self.assertEqual(len(masked), len(word))

4.    def test_mask_word_contains_underscores(self):
        """Masked word should contain underscores"""
        word = "CLAVES"
        masked = mask_word(word, reveal_count=2)
        self.assertIn("_", masked)

  
5.   def test_display_watermelon_valid_index(self):
        """display_watermelon should return a string for valid tries"""
        for i in range(5):
            stage = display_watermelon(i)
            self.assertIsInstance(stage, str)
