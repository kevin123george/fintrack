//package com.astra.fintrack.crons;
//
//import org.jsoup.Jsoup;
//import org.jsoup.nodes.Document;
//import org.jsoup.select.Elements;
//import org.jsoup.nodes.Element;
//import org.springframework.scheduling.annotation.Scheduled;
//import org.springframework.stereotype.Service;
//import java.io.IOException;
//import java.util.HashMap;
//import java.util.Map;
//
//@Service
//public class GoogleFinanceScraper {
//
//    private static final String SYMBOL = "META";
//    private static final String INDEX = "NASDAQ";
//    private static final String URL = "https://www.google.com/finance/quote/" + SYMBOL + ":" + INDEX + "?hl=en";
//
//    @Scheduled(fixedRate = 10000)
//    public void fetchStockData() {
//        try {
//            Document doc = Jsoup.connect(URL)
//                    .userAgent("Mozilla/5.0")
//                    .get();
//
//            Elements items = doc.select("div.gyFHrc");
//
//            Map<String, String> stockInfo = new HashMap<>();
//
//            for (Element item : items) {
//                String label = item.select("div.mfs7Fc").text();
//                String value = item.select("div.P6K39c").text();
//                stockInfo.put(label, value);
//            }
//
//            System.out.println("📈 " + SYMBOL + " Stats:");
//            stockInfo.forEach((k, v) -> System.out.println(k + ": " + v));
//
//            // You can now call your internal update API with these values
//            // e.g., using RestTemplate to post to http://localhost:8080/stocks/update
//
//        } catch (IOException e) {
//            System.err.println("❌ Error fetching data: " + e.getMessage());
//        }
//    }
//}
