//package com.astra.fintrack.dtos;
//
//import com.astra.fintrack.services.StockService;
//import org.springframework.scheduling.annotation.Scheduled;
//import org.springframework.stereotype.Service;
//
//import java.math.BigDecimal;
//
//@Service
//public class StockUpdaterJob {
//
//    // Replace with actual stock ID and conversion rate
//    private static final long STOCK_ID = 1;
//    private static final String SYMBOL = "AAPL";
//    private static final double USD_TO_EUR = 0.93;
//
//    private final StockService stockService;
//
//    public StockUpdaterJob(StockService stockService) {
//        this.stockService = stockService;
//    }
//
//    @Scheduled(fixedRate = 10000) // every 10 seconds
//    public void updateStockPrice() {
//        try {
//            Stock stock = YahooFinance.get(SYMBOL);
//            BigDecimal priceUSD = stock.getQuote().getPrice();
//            double priceEUR = priceUSD.doubleValue() * USD_TO_EUR;
//
//            System.out.printf("Updating %s to %.2f EUR%n", SYMBOL, priceEUR);
//            stockService.updatePrice(STOCK_ID, priceEUR);
//
//        } catch (Exception e) {
//            System.err.println("Failed to fetch or update stock: " + e.getMessage());
//        }
//    }
//}
