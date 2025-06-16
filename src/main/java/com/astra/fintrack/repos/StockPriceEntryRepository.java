package com.astra.fintrack.repos;

import com.astra.fintrack.model.StockPriceEntry;
import com.astra.fintrack.model.StockWatch;
import org.springframework.data.jdbc.repository.query.Query;
import org.springframework.data.jpa.repository.JpaRepository;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

public interface StockPriceEntryRepository extends JpaRepository<StockPriceEntry, Long> {

    // Find all price entries for a stock
    List<StockPriceEntry> findByStockSymbolOrderByTimestampAsc(String symbol);

//    // Optional: Get latest price entry for a stock
//    @Query("SELECT e FROM StockPriceEntry e WHERE e.stock.symbol = :symbol ORDER BY e.timestamp DESC LIMIT 1")
//    Optional<StockPriceEntry> findLatestBySymbol(String symbol);

    // Optional: Get price entries within a date range
    List<StockPriceEntry> findByStockAndTimestampBetween(StockWatch stock, LocalDateTime from, LocalDateTime to);

}