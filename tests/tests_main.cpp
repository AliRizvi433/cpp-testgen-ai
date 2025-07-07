#include "../src/main.cpp"
/*
#include "gtest/gtest.h"

namespace calculator {

TEST(CalculatorTest, AddMethodCorrectness1) {
  Calculator calc;
  EXPECT_EQ(3, calc.add(1, 2));
}

TEST(CalculatorTest, AddMethodCorrectness2) {
  Calculator calc;
  EXPECT_EQ(0, calc.add(0, 0));
}

TEST(CalculatorTest, AddMethodEdgeCase1) {
  Calculator calc;
  EXPECT_EQ(-1, calc.add(-2, 1));
}

TEST(CalculatorTest, AddMethodEdgeCase2) {
  Calculator calc;
  EXPECT_EQ(-3, calc.add(-2, -1));
}

} // namespace calculator
*/
#include "gtest/gtest.h"

#include <iostream>
#include "algorithm"

namespace calculator {

TEST(CalculatorTest, AddPositiveIntegers) {
  Calculator calc;
  EXPECT_EQ(3, calc.add(1, 2));
}

TEST(CalculatorTest, AddZero) {
  Calculator calc;
  EXPECT_EQ(0, calc.add(0, 0));
}

TEST(CalculatorTest, AddNegativeAndPositive) {
  Calculator calc;
  EXPECT_EQ(-1, calc.add(-2, 1));
}

TEST(CalculatorTest, AddTwoNegatives) {
  Calculator calc;
  EXPECT_EQ(-3, calc.add(-2, -1));
}

} // namespace calculator