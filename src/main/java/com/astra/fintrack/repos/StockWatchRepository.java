package com.astra.fintrack.repos;

import com.astra.fintrack.model.StockWatch;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface StockWatchRepository extends JpaRepository<StockWatch, String> {
    @Query("SELECT DISTINCT s.symbol FROM StockWatch s")
    List<String> findDistinctStockSymbols();
}
